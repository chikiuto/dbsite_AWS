(function() {
  const target     = document.getElementById('header'),
        height     = 112;
  let offset       = 0,
      lastPosition = 0,
      ticking      = false;

  function onScroll() {
    if (lastPosition > height) {
      if (lastPosition > offset) {
        target.classList.add('head-animation');
      } else {
        target.classList.remove('head-animation');
      }
      offset = lastPosition;
    }
  }

  window.addEventListener('scroll', function(e) {
    lastPosition = window.scrollY;
    if (!ticking) {
      window.requestAnimationFrame(function() {
        onScroll(lastPosition);
        ticking = false;
      });
      ticking = true;
    }
  });
})();


// const btn = document.querySelector('.btn-menu');
// const nav = document.querySelector('.list_nav_header');

// btn.addEventListener('click', () => {
//   nav.classList.toggle('open-menu');
//   if (btn.innerHTML === 'めにゅー') {
//     btn.innerHTML = '閉じる';
//   } else {
//     btn.innerHTML = 'めにゅー';
//   }
// });


let fadeInTarget = document.querySelectorAll('.fade-in');
window.addEventListener('scroll', () => {
  for (let i = 0; i < fadeInTarget.length; i++){
    const rect = fadeInTarget[i].getBoundingClientRect().top;
    const scroll = window.pageYOffset || document.documentElement.scrollTop;
    const offset = rect + scroll;
    const windowHeight = window.innerHeight; // 現在のブラウザの高さ
    if (scroll > offset - windowHeight + 250) {
      fadeInTarget[i].classList.add('scroll-in');
    }
  }
});

(function() {
  const image = document.querySelectorAll('.img-wrap');

  const observer = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (entry.intersectionRatio > 0) {
        entry.target.classList.add('img-animation');
      } else {
        entry.target.classList.remove('img-animation');
      }
    });
  });

  Array.prototype.forEach.call(image, function(img) {
    observer.observe(img);
  });
})();