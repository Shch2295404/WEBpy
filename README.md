# WEBpy
Introduction to Web Development

This code snippet is an HTML document that creates a simple webpage displaying information cards for users. 
The styling is defined in the embedded CSS between the <style> tags. 
It centers the content, styles the card layout with shadows and padding, 
  and defines styles for the individual elements inside the card such as images, headings, and paragraphs. 
The <body> section contains three user cards, each with an image, name, email, date of birth, 
  and city information inside a div element with the class "card".

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Информационные карточки пользователей</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-wrap: wrap;
            padding: 20px;
            background-color: #f0f0f0;
        }

        .card {
            width: 400px;
            border: 1px solid #ccc;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            background-color: #fff;
            margin: 20px;
            padding: 16px;
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .card:hover {
            transform: translateY(-10px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }

        .card img {
            width: 100%;
            height: auto;
            border-radius: 8px;
            margin-bottom: 16px;
        }

        .card h2 {
            font-size: 1.5em;
            margin: 0;
        }

        .card p {
            margin: 8px 0;
            color: #555;
        }
    </style>
</head>
<body>
    <div class="card">
        <img src="https://raw.githubusercontent.com/Shch2295404/WEBpy/289de2b659571a3e15a534cae25bc9b58b06b7f4/img/1.jpg" alt="Uer 1 Photo">
        <h2>Иванов Иван Иванович</h2>
        <p>Email: ivanov@mail.ru</p>
        <p>Дата рождения: 1970-01-01</p>
        <p>Город: Москва</p>
    </div>

    <div class="card">
        <img src="https://raw.githubusercontent.com/Shch2295404/WEBpy/289de2b659571a3e15a534cae25bc9b58b06b7f4/img/2.jpg" alt="User 2 Photo">
        <h2>Петров Петр Петрович</h2>
        <p>Email: petrov@@mail.ru</p>
        <p>Дата рождения: 1985-05-15</p>
        <p>Город: Санкт-Петербург</p>
    </div>

    <div class="card">
        <img src="https://raw.githubusercontent.com/Shch2295404/WEBpy/289de2b659571a3e15a534cae25bc9b58b06b7f4/img/3.jpg" alt="User 3 Photo">
        <h2>Сидорова Анна Сергеевна</h2>
        <p>Email: sidorova@@mail.ru</p>
        <p>Дата рождения: 1992-07-20</p>
        <p>Город: Казань</p>
    </div>
</body>
</html>
```

 This code snippet represents an HTML document displaying a list of Russian cuisine dishes with ratings, links to recipes, and images of the dishes. 
 The HTML includes styling for a table layout, 
 including borders, padding, background colors, and image sizes.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Рейтинг блюд русской кухни</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
        img {
            width: 100px;
            height: auto;
        }
    </style>
</head>
<body>
    <h1>Рейтинг блюд русской кухни</h1>
    <table>
        <thead>
            <tr>
                <th>Наименование блюда</th>
                <th>Рейтинг (от 1 до 10)</th>
                <th>Ссылка на рецепт</th>
                <th>Фото блюда</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Борщ</td>
                <td>9</td>
                <td><a href="https://www.tveda.ru/recepty/nastoyaschiy-borsch/" target="_blank">Recipe</a></td>
                <td><img src="https://cdn.tveda.ru/thumbs/c4c/c4cb83cd697482955737c62d87e88dcb/60ca468f96382e8e71c5c75917b6b0f1.jpg" alt="Борщ"></td>
            </tr>
            <tr>
                <td>Сырники</td>
                <td>8</td>
                <td><a href="https://www.tveda.ru/recepty/syrnicki/" target="_blank">Recipe</a></td>
                <td><img src="https://cdn.tveda.ru/thumbs/257/25767320c2daab2438511836951dfdbc/5a27df19095172bf07c1d5d7512c31a3.jpg" alt="Сырники"></td>
            </tr>
            <tr>
                <td>Котлеты</td>
                <td>7</td>
                <td><a href="https://www.tveda.ru/recepty/kotlety-s-kartofelnym-pyure/" target="_blank">Recipe</a></td>
                <td><img src="https://cdn.tveda.ru/thumbs/52b/52ba3a1a933efb0e4a47f2cf7785bc33/18459b061c7109ebd0785fe347870fbd.jpg" alt="Котлеты"></td>
            </tr>
            <tr>
                <td>Бефстроганов</td>
                <td>8.5</td>
                <td><a href="https://www.tveda.ru/recepty/befstroganov/" target="_blank">Recipe</a></td>
                <td><img src="https://cdn.tveda.ru/thumbs/6fa/6faf1f99b33d590afe06e4a2f1006e8c/2b838ff9a2d2805e0213c66a9c2be14a.jpg" alt="Бефстроганов"></td>
            </tr>
            <tr>
                <td>Щи</td>
                <td>7.5</td>
                <td><a href="https://www.tveda.ru/recepty/shchi-s-fasolyu-i-kopchyenymi-ryebrami/" target="_blank">Recipe</a></td>
                <td><img src="https://cdn.tveda.ru/thumbs/e15/e15ba0c3fd752f96457008569d8ac17a/86600ea17bd32050d93519e5aca4e779.jpg" alt="Щи"></td>
            </tr>
        </tbody>
    </table>
</body>
</html>
```
