document.getElementById('form').addEventListener('submit', function(event) {
    event.preventDefault();

    var district = document.getElementById('district').value;
    var age = document.getElementById('age').value;
    var type = document.getElementById('type').value;

    // ここで検索処理を行い、結果を表示します
    // 実際の検索処理はサーバーサイドで行う必要があります
    console.log('Search for:', district, age, type);
});
