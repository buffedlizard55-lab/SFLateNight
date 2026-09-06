const state = {
  venues: [],
  meta: {},
  transit: { lines: [] },
  query: '',
  day: 'all',
  category: 'all',
  neighborhood: 'all',
  cleanOnly: false,
  openId: null
};

const DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
const DAY_SHORT = { Friday: 'Fri', Saturday: 'Sat', Sunday: 'Sun' };
const ORIGIN = '21st Ave & Judah St, San Francisco, CA 94122';

const $ = (selector, parent = document) => parent.querySelector(selector);
const $$ = (selector, parent = document) => [...parent.querySelectorAll(selector)];

function escapeHtml(value = '') {
  return String(value).replace(/[&<>'"]/g, (character) => ({
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    "'": '&#39;',
    '"': '&quot;'
  }[character]));
}

function routeUrl(address) {
  const params = new URLSearchParams({
    api: '1',
    origin: ORIGIN,
    destination: address,
    travelmode: 'transit'
  });
  return `https://www.google.com/maps/dir/?${params.toString()}`;
}

function mapUrl(address) {
  return `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(address)}`;
}

function lineMap() {
  return new Map((state.transit.lines || []).map((line) => [line.id, line]));
}

function venueLines(venue) {
  const lines = lineMap();
  return (venue.access.lineIds || []).map((id) => lines.get(id)).filter(Boolean);
}

function neighborhoodInfo(groupId) {
  return (state.meta.neighborhoodGroups || []).find((group) => group.id === groupId) || {
    id: groupId,
    label: groupId,
    description: ''
  };
}

function neighborhoodLabel(groupId) {
  return neighborhoodInfo(groupId).label;
}

function venueGroupId(venue) {
  return venue.neighborhoodGroup || venue.neighborhood;
}

function statusBadge(venue) {
  if (venue.verification.status === 'verified') {
    return '<span class="status-badge verified">Official match</span>';
  }
  return '<span class="status-badge gap">Review gap</span>';
}

function shortLateHours(hours) {
  const first = hours.split(';')[0].trim();
  return first
    .replace(/:00/g, '')
    .replace(/\s*PM/g, 'p')
    .replace(/\s*AM/g, 'a')
    .replace(/\s+–\s+/g, '–');
}

function filteredVenues() {
  const query = state.query.trim().toLowerCase();
  const lines = lineMap();
  return state.venues.filter((venue) => {
    const venueLineText = (venue.access.lineIds || [])
      .map((id) => {
        const line = lines.get(id);
        return line ? `${line.id} ${line.name} ${line.mode}` : id;
      })
      .join(' ');
    const haystack = [
      venue.name,
      venue.category,
      venue.neighborhood,
      neighborhoodLabel(venueGroupId(venue)),
      venue.address,
      venue.access.summary,
      venue.access.detail,
      venueLineText,
      ...venue.flags
    ].join(' ').toLowerCase();
    const queryMatch = !query || haystack.includes(query);
    const dayMatch = state.day === 'all' || venue.qualifyingDays.includes(state.day);
    const categoryMatch = state.category === 'all' || venue.category === state.category;
    const neighborhoodMatch = state.neighborhood === 'all' || venueGroupId(venue) === state.neighborhood;
    const cleanMatch = !state.cleanOnly || venue.verification.status === 'verified';
    return queryMatch && dayMatch && categoryMatch && neighborhoodMatch && cleanMatch;
  });
}

function renderLateDays(venue) {
  return `<div class="late-day-list">${venue.qualifyingDays.map((day) => `
    <div class="late-day"><strong>${DAY_SHORT[day]}</strong><span>${escapeHtml(shortLateHours(venue.hours[day]))}</span></div>
  `).join('')}</div>`;
}

function renderFullHours(venue) {
  return `<dl class="full-hours">${DAYS.map((day) => `
    <div><dt>${day}</dt><dd>${escapeHtml(venue.hours[day])}</dd></div>
  `).join('')}</dl>`;
}

function renderLinePills(venue) {
  return `<div class="transit-line-pills">${venueLines(venue).map((line) => `
    <a class="transit-line-pill" href="${escapeHtml(line.routeUrl)}" target="_blank" rel="noopener noreferrer" title="Open official ${escapeHtml(line.name)} route page">${escapeHtml(line.id)}</a>
  `).join('')}</div>`;
}

function renderVenueServiceWindows(venue) {
  const lines = venueLines(venue);
  if (!lines.length) return '<span class="access-subnote">Transit line not mapped; use the live planner.</span>';
  return `<div class="transit-mini-list">${lines.map((line) => `
    <span><strong>${escapeHtml(line.id)}</strong> ${escapeHtml(line.todayWindow)}</span>
  `).join('')}</div>`;
}

function renderTransitDetails(venue) {
  const lines = venueLines(venue);
  if (!lines.length) {
    return '<p class="access-subnote">No route window was transcribed for this row. Use the live planner and the venue source before leaving.</p>';
  }
  return `<div class="transit-detail-list">${lines.map((line) => `
    <div class="transit-detail-item">
      <div><a href="${escapeHtml(line.routeUrl)}" target="_blank" rel="noopener noreferrer"><strong>${escapeHtml(line.id)}</strong> ${escapeHtml(line.name)} ↗</a><span>${escapeHtml(line.mode)}</span></div>
      <p><strong>${escapeHtml(line.todayWindow)}</strong><br />${escapeHtml(line.todayFrequency)}</p>
      <small>${escapeHtml(line.nightCoverage)}</small>
    </div>
  `).join('')}</div>`;
}

function renderSources(venue) {
  const official = `<a href="${escapeHtml(venue.officialUrl)}" target="_blank" rel="noopener noreferrer">Official venue page <span aria-hidden="true">↗</span></a>`;
  const map = `<a href="${mapUrl(venue.address)}" target="_blank" rel="noopener noreferrer">Open location map <span aria-hidden="true">↗</span></a>`;
  const route = `<a href="${routeUrl(venue.address)}" target="_blank" rel="noopener noreferrer">Transit + walk route <span aria-hidden="true">↗</span></a>`;
  const transitSource = venue.access.sources?.[0];
  const transit = transitSource
    ? `<a href="${escapeHtml(transitSource.url)}" target="_blank" rel="noopener noreferrer">${escapeHtml(transitSource.label)} <span aria-hidden="true">↗</span></a>`
    : '';
  return `${official}${map}${route}${transit}`;
}

function renderNeighborhoodHeader(groupId, venues) {
  const info = neighborhoodInfo(groupId);
  const lineIds = [...new Set(venues.flatMap((venue) => venue.access.lineIds || []))];
  return `
    <tr class="neighborhood-row">
      <th colspan="6" scope="rowgroup" id="cluster-${escapeHtml(groupId)}">
        <div class="neighborhood-heading-line">
          <div><span class="neighborhood-kicker">Neighborhood cluster</span><strong>${escapeHtml(info.label)}</strong></div>
          <span class="neighborhood-count">${venues.length} ${venues.length === 1 ? 'place' : 'places'}</span>
          <span class="neighborhood-lines">Muni: ${escapeHtml(lineIds.join(' · ') || 'live planner')}<a class="neighborhood-back" href="#directory">↑ clusters</a></span>
        </div>
        <span class="neighborhood-description">${escapeHtml(info.description)}</span>
      </th>
    </tr>
  `;
}

function renderVenueRow(venue, index) {
  const isOpen = state.openId === venue.id;
  return `
    <tr class="main-row${isOpen ? ' has-details-open' : ''}" data-venue-id="${escapeHtml(venue.id)}">
      <td>
        <div class="place-name">
          <span class="place-index">${String(index).padStart(2, '0')}</span>
          <div>
            <h3>${escapeHtml(venue.name)}</h3>
            <div class="place-meta"><span class="type-badge">${escapeHtml(venue.category)}</span><span class="neighborhood-badge">${escapeHtml(venue.neighborhood)}</span></div>
          </div>
        </div>
      </td>
      <td>${renderLateDays(venue)}</td>
      <td>
        <div class="address-block">
          <p>${escapeHtml(venue.address)}</p>
          <a class="address-link" href="${mapUrl(venue.address)}" target="_blank" rel="noopener noreferrer">Map <span aria-hidden="true">↗</span></a>
        </div>
      </td>
      <td>
        <div class="access-block">
          <p>${escapeHtml(venue.access.summary)}</p>
          ${renderLinePills(venue)}
          ${renderVenueServiceWindows(venue)}
          <span class="access-subnote">${escapeHtml(venue.access.detail)}</span>
          <a class="route-link" href="${routeUrl(venue.address)}" target="_blank" rel="noopener noreferrer">Plan live route <span aria-hidden="true">↗</span></a>
        </div>
      </td>
      <td>${statusBadge(venue)}<a class="source-link" href="${escapeHtml(venue.source.url)}" target="_blank" rel="noopener noreferrer">Source line <span aria-hidden="true">↗</span></a></td>
      <td><button class="details-button${isOpen ? ' is-open' : ''}" type="button" aria-expanded="${isOpen}" aria-controls="details-${escapeHtml(venue.id)}" data-details-id="${escapeHtml(venue.id)}" title="${isOpen ? 'Hide' : 'Show'} full hours and source quote"><span aria-hidden="true">＋</span><span class="sr-only">${isOpen ? 'Hide' : 'Show'} details for ${escapeHtml(venue.name)}</span></button></td>
    </tr>
    <tr class="details-row${isOpen ? ' is-open' : ''}" id="details-${escapeHtml(venue.id)}" data-detail-row="${escapeHtml(venue.id)}">
      <td colspan="6">
        <div class="details-inner">
          <div>
            <p class="detail-heading">Full weekly hours</p>
            ${renderFullHours(venue)}
          </div>
          <div>
            <p class="detail-heading">Official line for manual review</p>
            <blockquote class="quote">“${escapeHtml(venue.source.quote)}”</blockquote>
            <div class="source-actions">${renderSources(venue)}</div>
          </div>
          <div>
            <p class="detail-heading">Transit lines · ${escapeHtml(state.transit.snapshotDay || 'snapshot')}</p>
            ${renderTransitDetails(venue)}
          </div>
          <div>
            <p class="detail-heading">Notes to check</p>
            <ul class="flag-list">${venue.flags.map((flag) => `<li>${escapeHtml(flag)}</li>`).join('')}</ul>
          </div>
        </div>
      </td>
    </tr>
  `;
}

function groupVenues(venues) {
  const groups = new Map();
  venues.forEach((venue) => {
    const id = venueGroupId(venue);
    if (!groups.has(id)) groups.set(id, []);
    groups.get(id).push(venue);
  });
  const configuredOrder = new Map((state.meta.neighborhoodGroups || []).map((group, index) => [group.id, index]));
  return [...groups.entries()].sort(([a], [b]) => {
    const orderA = configuredOrder.has(a) ? configuredOrder.get(a) : 999;
    const orderB = configuredOrder.has(b) ? configuredOrder.get(b) : 999;
    return orderA - orderB || neighborhoodLabel(a).localeCompare(neighborhoodLabel(b));
  });
}

function renderVenueRows(venues) {
  const tbody = $('#venue-table-body');
  if (!venues.length) {
    tbody.innerHTML = '';
    $('#empty-state').hidden = false;
    renderClusterNav([]);
    return;
  }
  $('#empty-state').hidden = true;
  let index = 0;
  const grouped = groupVenues(venues);
  tbody.innerHTML = grouped.map(([groupId, group]) => {
    const header = renderNeighborhoodHeader(groupId, group);
    const rows = group.map((venue) => renderVenueRow(venue, ++index)).join('');
    return `${header}${rows}`;
  }).join('');
  renderClusterNav(grouped);
}

function renderClusterNav(grouped) {
  const nav = $('#cluster-nav');
  if (!nav) return;
  nav.innerHTML = grouped.map(([groupId, group]) => `
    <a href="#cluster-${escapeHtml(groupId)}">${escapeHtml(neighborhoodLabel(groupId))} <span>${group.length}</span></a>
  `).join('');
}

function renderFlags() {
  const flagItems = state.venues.flatMap((venue) => venue.flags.map((flag) => ({ venue, flag })));
  $('#flag-count').textContent = `${flagItems.length} ${flagItems.length === 1 ? 'note' : 'notes'}`;
  $('#flags-grid').innerHTML = flagItems.map(({ venue, flag }) => `
    <article class="flag-card">
      <span class="flag-card-icon" aria-hidden="true">!</span>
      <div>
        <h3>${escapeHtml(venue.name)}</h3>
        <p>${escapeHtml(flag)}</p>
        <a href="${escapeHtml(venue.source.url)}" target="_blank" rel="noopener noreferrer">Review official source ↗</a>
      </div>
    </article>
  `).join('');
}

function formatSnapshotDate(dateString) {
  const [year, month, day] = dateString.split('-').map(Number);
  return new Intl.DateTimeFormat('en-US', {
    timeZone: state.transit.timezone || 'America/Los_Angeles',
    year: 'numeric', month: 'long', day: 'numeric'
  }).format(new Date(Date.UTC(year, month - 1, day, 12)));
}

function todayInTimezone() {
  const parts = new Intl.DateTimeFormat('en-US', {
    timeZone: state.transit.timezone || 'America/Los_Angeles',
    year: 'numeric', month: '2-digit', day: '2-digit'
  }).formatToParts(new Date());
  const values = Object.fromEntries(parts.map((part) => [part.type, part.value]));
  return `${values.year}-${values.month}-${values.day}`;
}

function renderTransitDirectory() {
  const transit = state.transit;
  const snapshotDate = formatSnapshotDate(transit.snapshotDate);
  $('#transit-date').textContent = snapshotDate;
  $('#transit-day').textContent = `${transit.snapshotDay} service · ${transit.timezone}`;
  $('#transit-origin-note').textContent = transit.originNote;
  const currentDate = todayInTimezone();
  const isCurrentSnapshot = currentDate === transit.snapshotDate;
  const alert = $('#transit-alert');
  alert.hidden = isCurrentSnapshot;
  if (!isCurrentSnapshot) {
    alert.innerHTML = `<strong>This is a dated service snapshot.</strong> The route table was checked ${escapeHtml(snapshotDate)}; your current local date is ${escapeHtml(formatSnapshotDate(currentDate))}. Use the official route pages and alerts before treating any window as current.`;
  }
  const orderedLines = [...transit.lines].sort((a, b) => {
    const rank = (line) => (/24 hours/i.test(line.todayWindow) ? 0 : /nightly/i.test(line.todayWindow) ? 1 : 2);
    return rank(a) - rank(b) || String(a.id).localeCompare(String(b.id), undefined, { numeric: true });
  });
  $('#transit-grid').innerHTML = orderedLines.map((line) => `
    <article class="transit-card">
      <div class="transit-card-top">
        <a class="transit-route-id" href="${escapeHtml(line.routeUrl)}" target="_blank" rel="noopener noreferrer">${escapeHtml(line.id)}</a>
        <div><h3>${escapeHtml(line.name)}</h3><span>${escapeHtml(line.mode)}</span></div>
      </div>
      <p class="transit-window-label">${escapeHtml(transit.snapshotDay)} service window</p>
      <strong class="transit-window">${escapeHtml(line.todayWindow)}</strong>
      <p class="transit-frequency">${escapeHtml(line.todayFrequency)}</p>
      <p class="transit-night"><span>Night coverage</span>${escapeHtml(line.nightCoverage)}</p>
      <div class="transit-card-links"><a href="${escapeHtml(line.routeUrl)}" target="_blank" rel="noopener noreferrer">Official route ↗</a><a href="${escapeHtml(line.scheduleUrl)}" target="_blank" rel="noopener noreferrer">Saturday timetable ↗</a></div>
    </article>
  `).join('');
}

function updateActiveFilterLine(visibleCount) {
  const line = $('#active-filter-line');
  const parts = [];
  if (state.query) parts.push(`“${state.query}”`);
  if (state.day !== 'all') parts.push(`late on ${state.day}`);
  if (state.category !== 'all') parts.push(state.category);
  if (state.neighborhood !== 'all') parts.push(neighborhoodLabel(state.neighborhood));
  if (state.cleanOnly) parts.push('clean matches only');
  line.hidden = parts.length === 0;
  if (parts.length) {
    $('#active-filter-copy').textContent = `${parts.join(' · ')} · ${visibleCount} ${visibleCount === 1 ? 'result' : 'results'}`;
  }
}

function render() {
  const venues = filteredVenues();
  renderVenueRows(venues);
  $('#result-count').textContent = `${venues.length} ${venues.length === 1 ? 'place' : 'places'}`;
  updateActiveFilterLine(venues.length);
}

function clearFilters() {
  state.query = '';
  state.day = 'all';
  state.category = 'all';
  state.neighborhood = 'all';
  state.cleanOnly = false;
  $('#search-input').value = '';
  $('#category-select').value = 'all';
  $('#neighborhood-select').value = 'all';
  $('#review-toggle').checked = false;
  $$('.filter-chip').forEach((button) => button.classList.toggle('is-active', button.dataset.day === 'all'));
  render();
}

function bindControls() {
  $('#search-input').addEventListener('input', (event) => {
    state.query = event.target.value;
    render();
  });
  $$('.filter-chip').forEach((button) => {
    button.addEventListener('click', () => {
      state.day = button.dataset.day;
      $$('.filter-chip').forEach((item) => item.classList.toggle('is-active', item === button));
      render();
    });
  });
  $('#category-select').addEventListener('change', (event) => {
    state.category = event.target.value;
    render();
  });
  $('#neighborhood-select').addEventListener('change', (event) => {
    state.neighborhood = event.target.value;
    render();
  });
  $('#review-toggle').addEventListener('change', (event) => {
    state.cleanOnly = event.target.checked;
    render();
  });
  $('#clear-filters').addEventListener('click', clearFilters);
  $('#empty-clear').addEventListener('click', clearFilters);
  $('#venue-table-body').addEventListener('click', (event) => {
    const button = event.target.closest('[data-details-id]');
    if (!button) return;
    const id = button.dataset.detailsId;
    state.openId = state.openId === id ? null : id;
    render();
    if (state.openId) {
      requestAnimationFrame(() => {
        const row = document.querySelector(`[data-detail-row="${CSS.escape(state.openId)}"]`);
        if (row && window.innerWidth < 760) row.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
      });
    }
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === '/' && document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') {
      event.preventDefault();
      $('#search-input').focus();
    }
    if (event.key === 'Escape' && document.activeElement === $('#search-input')) {
      $('#search-input').value = '';
      state.query = '';
      render();
    }
  });
}

async function init() {
  try {
    const response = await fetch('data/venues.json');
    if (!response.ok) throw new Error(`Data request failed: ${response.status}`);
    const data = await response.json();
    state.meta = data.meta;
    state.transit = data.meta.transit;
    state.venues = data.venues;
    const categories = [...new Set(state.venues.map((venue) => venue.category))].sort((a, b) => a.localeCompare(b));
    $('#category-select').insertAdjacentHTML('beforeend', categories.map((category) => `<option value="${escapeHtml(category)}">${escapeHtml(category)}</option>`).join(''));
    const groups = data.meta.neighborhoodGroups || [];
    $('#neighborhood-select').insertAdjacentHTML('beforeend', groups.map((group) => `<option value="${escapeHtml(group.id)}">${escapeHtml(group.label)}</option>`).join(''));
    const cleanCount = state.venues.filter((venue) => venue.verification.status === 'verified').length;
    $('#hero-total').textContent = data.meta.recordCount;
    $('#hero-verified').textContent = cleanCount;
    $('#hero-verified').nextElementSibling.textContent = 'clean matches';
    renderTransitDirectory();
    renderFlags();
    bindControls();
    render();
  } catch (error) {
    console.error(error);
    $('#venue-table-body').innerHTML = `<tr><td colspan="6"><div class="empty-state"><span class="empty-icon" aria-hidden="true">!</span><h3>Directory data could not load.</h3><p>Open <a href="data/venues.json">the raw data file</a> to review the source-linked records.</p></div></td></tr>`;
    $('#result-count').textContent = 'Data unavailable';
  }
}

init();
