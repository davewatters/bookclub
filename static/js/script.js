"use strict";

/**
 * Dismiss system messages alert
 */
setTimeout(function () {
  let messages = document.getElementById('msg');
  let alert = new bootstrap.Alert(messages);
  alert.close();
}, 2500);


/**
 * Event Listeners
 */
