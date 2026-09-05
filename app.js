const state = {
  venues: [],
  query: '',
  day: 'all',
  category: 'all',
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
  return state.venues.filter((venue) => {
    const haystack = [
      venue.name,
      venue.category,
      venue.neighborhood,
      venue.address,
      venue.access.summary,
      venue.access.detail,
      ...venue.flags
    ].join(' ').toLowerCase();
    const queryMatch = !query || haystack.includes(query);
    const dayMatch = state.day === 'all' || venue.qualifyingDays.includes(state.day);
    const categoryMatch = state.category === 'all' || venue.category === state.category;
    const cleanMatch = !state.cleanOnly || venue.verification.status === 'verified';
    return queryMatch && dayMatch && categoryMatch && cleanMatch;
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

function renderSources(venue) {
  const official = `<a href="${escapeHtml(venue.officialUrl)}" target="_blank" rel="noopener noreferrer">Official venue page <span aria-hidden="true">↗</span></a>`;
  const map = `<a href="${mapUrl(venue.address)}" target="_blank" rel="noopener noreferrer">Open location map <span aria-hidden="true">↗</span></a>`;
  const route = `<a href="${routeUrl(venue.address)}" target="_blank" rel="noopener noreferrer">Transit + walk route <span aria-hidden="true">↗</span></a>`;
  const transitSource = venue.access.sources[0];
  const transit = `<a href="${escapeHtml(transitSource.url)}" target="_blank" rel="noopener noreferrer">${escapeHtml(transitSource.label)} <span aria-hidden="true">↗</span></a>`;
  return `${official}${map}${route}${transit}`;
}

function renderVenueRows(venues) {
  const tbody = $('#venue-table-body');
  if (!venues.length) {
    tbody.innerHTML = '';
    $('#empty-state').hidden = false;
    return;
  }
  $('#empty-state').hidden = true;
  tbody.innerHTML = venues.map((venue, index) => {
    const status = venue.verification.status === 'verified' ? 'verified' : 'gap';
    const isOpen = state.openId === venue.id;
    return `
      <tr class="main-row${isOpen ? ' has-details-open' : ''}" data-venue-id="${escapeHtml(venue.id)}">
        <td>
          <div class="place-name">
            <span class="place-index">${String(index + 1).padStart(2, '0')}</span>
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
              <p class="detail-heading">Notes to check</p>
              <ul class="flag-list">${venue.flags.map((flag) => `<li>${escapeHtml(flag)}</li>`).join('')}</ul>
            </div>
          </div>
        </td>
      </tr>
    `;
  }).join('');
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

function updateActiveFilterLine(visibleCount) {
  const line = $('#active-filter-line');
  const parts = [];
  if (state.query) parts.push(`“${state.query}”`);
  if (state.day !== 'all') parts.push(`late on ${state.day}`);
  if (state.category !== 'all') parts.push(state.category);
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
  state.cleanOnly = false;
  $('#search-input').value = '';
  $('#category-select').value = 'all';
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
    state.venues = data.venues;
    const categories = [...new Set(state.venues.map((venue) => venue.category))].sort((a, b) => a.localeCompare(b));
    $('#category-select').insertAdjacentHTML('beforeend', categories.map((category) => `<option value="${escapeHtml(category)}">${escapeHtml(category)}</option>`).join(''));
    const cleanCount = state.venues.filter((venue) => venue.verification.status === 'verified').length;
    $('#hero-total').textContent = data.meta.recordCount;
    $('#hero-verified').textContent = cleanCount;
    $('#hero-verified').nextElementSibling.textContent = 'clean matches';
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
