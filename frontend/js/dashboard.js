const API_URL = 'http://localhost:8080/api';
const token = localStorage.getItem('token');
const username = localStorage.getItem('username');

// Check authentication
if (!token) {
    window.location.href = 'index.html';
}

// Display username
document.getElementById('username').textContent = username;

// Load user preferences on page load
window.addEventListener('load', () => {
    loadPreferences();
});

async function loadPreferences() {
    try {
        const response = await fetch(`${API_URL}/preferences`, {
            headers: { 'Authorization': `Bearer ${token}` }
        });

        if (response.ok) {
            const preferences = await response.json();
            displayPreferences(preferences);
        }
    } catch (error) {
        console.error('Error loading preferences:', error);
    }
}

function displayPreferences(preferences) {
    const container = document.getElementById('preferencesList');

    if (preferences.length === 0) {
        container.innerHTML = '<p class="text-muted">No preferences yet. Add some to get personalized recommendations!</p>';
        return;
    }

    container.innerHTML = preferences.map(pref => `
        <span class="badge badge-category me-2 mb-2">
            ${pref.category} <span class="badge bg-light text-dark">${pref.weight}</span>
        </span>
    `).join('');
}

async function addPreference() {
    const category = document.getElementById('preferenceCategory').value;
    const weight = parseFloat(document.getElementById('preferenceWeight').value);

    try {
        const response = await fetch(`${API_URL}/preferences`, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ category, weight })
        });

        if (response.ok) {
            // Close modal
            const modal = bootstrap.Modal.getInstance(document.getElementById('addPreferenceModal'));
            modal.hide();

            // Reset form
            document.getElementById('preferenceForm').reset();

            // Reload preferences
            loadPreferences();
        }
    } catch (error) {
        console.error('Error adding preference:', error);
    }
}

async function loadRecommendations() {
    const container = document.getElementById('recommendationsList');
    container.innerHTML = '<div class="col-12 text-center py-5"><div class="spinner-border text-primary"></div></div>';

    try {
        const response = await fetch(`${API_URL}/recommendations`, {
            headers: { 'Authorization': `Bearer ${token}` }
        });

        if (response.ok) {
            const items = await response.json();
            displayRecommendations(items);
        }
    } catch (error) {
        console.error('Error loading recommendations:', error);
        container.innerHTML = '<div class="col-12 text-center text-danger">Failed to load recommendations</div>';
    }
}

function displayRecommendations(items) {
    const container = document.getElementById('recommendationsList');

    if (items.length === 0) {
        container.innerHTML = '<div class="col-12 text-center text-muted py-5">No recommendations available. Try adding more preferences!</div>';
        return;
    }

    container.innerHTML = items.map(item => `
        <div class="col-md-4 mb-4">
            <div class="card item-card">
                <div class="card-body">
                    <h5 class="card-title">${item.title}</h5>
                    <p class="card-text text-muted">${item.description || 'No description'}</p>
                    <div class="d-flex justify-content-between align-items-center">
                        <span class="badge badge-category">${item.category}</span>
                        <small class="text-muted"><i class="fas fa-tags"></i> ${item.tags || 'N/A'}</small>
                    </div>
                </div>
            </div>
        </div>
    `).join('');
}

function logout() {
    localStorage.clear();
    window.location.href = 'index.html';
}
