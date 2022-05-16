var debouncer window.addEventListener('scroll', function (e) { if (debouncer) { clearTimeout(debouncer); } debouncer = setTimeout(function() { console.log('스크롤 이벤트 발생!'); const count = document.getElementById('count'); count.innerText = parseInt(count.innerText) + 1 }, 300); })

출처: https://programming119.tistory.com/241 [개발자 아저씨들 힘을모아]