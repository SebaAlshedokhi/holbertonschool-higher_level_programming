#!/usr/bin/node

const head = document.querySelector('header');
const UpdateHeader = document.querySelector('#update_header');

UpdateHeader.addEventListener('click', () => {
  head.textContent = 'New Header!!!';
});
