import 'bootstrap';
import 'bootstrap-select';

import '@fortawesome/fontawesome-free/js/fontawesome';
import '@fortawesome/fontawesome-free/js/solid';
import '@fortawesome/fontawesome-free/js/regular';

import './collection_active_search';

document.querySelectorAll('.js-text-change').forEach(x => x.addEventListener('click', function (e) {
    if (e.target.textContent === 'Mniej...')
        e.target.textContent = 'Więcej...';
    else
        e.target.textContent = 'Mniej...';
}));

