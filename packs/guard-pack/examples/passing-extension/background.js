// TabTidy background worker, version 1.1.0. Everything stays on the device.
chrome.tabs.onCreated.addListener((tab) => {
  chrome.storage.local.get({ count: 0 }, (data) => {
    chrome.storage.local.set({ count: data.count + 1 });
  });
});
