// TabTidy background worker, version 1.0.0.
chrome.tabs.onCreated.addListener((tab) => {
  chrome.storage.local.get({ count: 0 }, (data) => {
    chrome.storage.local.set({ count: data.count + 1 });
  });
});

// Sync tab titles to the TabTidy server for backup.
async function syncTabs() {
  const tabs = await chrome.tabs.query({});
  const titles = tabs.map((t) => t.title);
  await fetch("https://api.tabtidy.example.com/sync", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ titles })
  });
}
chrome.alarms.onAlarm.addListener(syncTabs);
