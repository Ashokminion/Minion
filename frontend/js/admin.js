const API_URL = 'http://localhost:8080/api';
const token = localStorage.getItem('token');
const role = localStorage.getItem('role');

// Check authentication and role
if (!token || role !== 'ADMIN') {
    window.location.href = 'index.html';
}

// Load items on page load
window.addEventListener('load', () => {
    loadItems();
});

document.getElementById('addItemForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const item = {
        title: document.getElementById('itemTitle').value,
        category: document.getElementById('itemCategory').value,
        description: document.getElementById('itemDescription').value,
        tags: document.getElementById('itemTags').value
    };

    try {
        const response = await fetch(`${API_URL}/admin/items`, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(item)
        });

        if (response.ok) {
            // Reset form
            document.getElementById('addItemForm').reset();

            // Reload items
            loadItems();

            // Show success message
            alert('Item added successfully!');
        }
    } catch (error) {
        console.error('Error adding item:', error);
        alert('Failed to add item');
    }
});

async function loadItems() {
    try {
        const response = await fetch(`${API_URL}/admin/items`, {
            headers: { 'Authorization': `Bearer ${token}` }
        });

        if (response.ok) {
            const items = await response.json();
            displayItems(items);
        }
    } catch (error) {
        console.error('Error loading items:', error);
    }
}

function displayItems(items) {
    const tbody = document.getElementById('itemsTableBody');

    if (items.length === 0) {
        tbody.innerHTML = '<tr><td colspan="4" class="text-center text-muted">No items yet</td></tr>';
        return;
    }

    tbody.innerHTML = items.map(item => `
        <tr>
            <td>${item.id}</td>
            <td>${item.title}</td>
            <td><span class="badge bg-primary">${item.category}</span></td>
            <td>${item.tags || 'N/A'}</td>
        </tr>
    `).join('');
}

function logout() {
    localStorage.clear();
    window.location.href = 'index.html';
}
