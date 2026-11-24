document.addEventListener("DOMContentLoaded", async () => {
  const tabs = await chrome.tabs.query({ currentWindow: true });
  const list = document.createElement("p");
  list.textContent = tabs.length + " tabs open in this window.";
  document.body.appendChild(list);
});
