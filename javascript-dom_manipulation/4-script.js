#!/usr/bin/node

const item = document.querySelector('#add_item');
const list = document.querySelector('.my_list');

item.addEventListener('click', () => {
  const newElement = document.createElement('li');  //createElement just with doc not element
  newElement.textContent = 'Item';
  list.appendChild(newElement);
});
