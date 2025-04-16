
let editingRow = null;

function openNewPostModal() {
  editingRow = null;
  document.getElementById('modalTitle').innerText = 'New Post';
  document.getElementById('postTitle').value = '';
  document.getElementById('postComment').value = '';
  document.getElementById('postModal').style.display = 'block';
  document.getElementById('overlay').style.display = 'block';
}

function openEditModal(btn) {
  editingRow = btn.closest('tr');
  const title = editingRow.children[0].innerText;
  const comment = editingRow.children[1].innerText;
  document.getElementById('modalTitle').innerText = 'Edit Post';
  document.getElementById('postTitle').value = title;
  document.getElementById('postComment').value = comment;
  document.getElementById('postModal').style.display = 'block';
  document.getElementById('overlay').style.display = 'block';
}

function savePost() {
  const title = document.getElementById('postTitle').value;
  const comment = document.getElementById('postComment').value;

  if (editingRow) {
    editingRow.children[0].innerText = title;
    editingRow.children[1].innerText = comment;
    alert('Post updated successfully.');
  } else {
    const table = document.getElementById('postsTable');
    const newRow = document.createElement('tr');
    newRow.innerHTML = `<td>${title}</td><td>${comment}</td><td>
      <button class="btn btn-edit" onclick="openEditModal(this)">✏️ Edit</button>
      <button class="btn btn-delete" onclick="deletePost(this)">🗑️ Delete</button></td>`;
    table.appendChild(newRow);
    alert('Post created successfully.');
  }
  closeModal();
}

function deletePost(btn) {
  const row = btn.closest('tr');
  row.remove();
  alert('Post deleted successfully.');
}

function closeModal() {
  document.getElementById('postModal').style.display = 'none';
  document.getElementById('overlay').style.display = 'none';
}
document.getElementById('overlay')?.addEventListener('click', closeModal);

function openNewUserModal() {
  editingRow = null;
  document.getElementById('modalTitle').innerText = 'New User';
  document.getElementById('userName').value = '';
  document.getElementById('userEmail').value = '';
  document.getElementById('userModal').style.display = 'block';
  document.getElementById('overlay').style.display = 'block';
}

function saveUser() {
  const username = document.getElementById('userName').value;
  const email = document.getElementById('userEmail').value;

  if (editingRow) {
    editingRow.children[0].innerText = username;
    editingRow.children[1].innerText = email;
    alert('User updated successfully.');
  } else {
    const table = document.getElementById('usersTable');
    const newRow = document.createElement('tr');
    newRow.innerHTML = `<td>${username}</td><td>${email}</td><td>
      <button class="btn btn-edit" onclick="openEditModal(this)">✏️ Edit</button>
      <button class="btn btn-delete" onclick="deleteUser(this)">🗑️ Delete</button></td>`;
    table.appendChild(newRow);
    alert('User added successfully.');
  }
  closeModal();
}

function deleteUser(btn) {
  const row = btn.closest('tr');
  row.remove();
  alert('User deleted successfully.');
}
