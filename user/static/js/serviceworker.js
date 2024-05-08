// var staticCacheName = 'djangopwa-v1';

// self.addEventListener('install', function(event) {
//   event.waitUntil(
//     caches.open(staticCacheName).then(function(cache) {
//       return cache.addAll([
//         '/'
//       ]);
//     })
//   );
// });

// self.addEventListener('fetch', function(event) {
//   var requestUrl = new URL(event.request.url);
//     if (requestUrl.origin === location.origin) {
//       if ((requestUrl.pathname === '/')) {
//         event.respondWith(caches.match('/'));
//         return;
//       }
//     }
//     event.respondWith(
//       caches.match(event.request).then(function(response) {
//         return response || fetch(event.request);
//       })
//     );
// });

// if ('serviceWorker' in navigator) {
//    console.log("Will the service worker register?");
//    navigator.serviceWorker.register('service-worker.js')
//      .then(function(reg){
//        console.log("Yes, it did.");
//     }).catch(function(err) {
//        console.log("No it didn't. This happened:", err)
//    });
// }