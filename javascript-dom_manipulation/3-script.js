#!/usr/bin/node

const head = document.querySelector('header');
const togg = document.querySelector('#toggle_header');

togg.addEventListener('click', () => {
  if(head.classList.contains('red'))
  {
    head.classList.remove('red');
    head.classList.add('green');
  }
  else
  {
    head.classList.remove('green');
    head.classList.add('red');
  };
});
