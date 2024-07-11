# WEBpy
Introduction to Web Development

 This code snippet represents an HTML document displaying a list of Russian cuisine dishes with ratings, links to recipes, and images of the dishes. 
 The HTML includes styling for a table layout, 
 including borders, padding, background colors, and image sizes.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Russian Cuisine Ratings</title>
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
                <th>Name of the Dish</th>
                <th>Rating (1 to 10)</th>
                <th>Link to Recipe</th>
                <th>Photo of the Dish</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Borscht</td>
                <td>9</td>
                <td><a href="https://www.example.com/borscht-recipe" target="_blank">Recipe</a></td>
                <td><img src="https://www.example.com/images/borscht.jpg" alt="Борщ"></td>
            </tr>
            <tr>
                <td>Pelmeni</td>
                <td>8</td>
                <td><a href="https://www.example.com/pelmeni-recipe" target="_blank">Recipe</a></td>
                <td><img src="https://www.example.com/images/pelmeni.jpg" alt="Пельмени"></td>
            </tr>
            <tr>
                <td>Blini</td>
                <td>7</td>
                <td><a href="https://www.example.com/blini-recipe" target="_blank">Recipe</a></td>
                <td><img src="https://www.example.com/images/blini.jpg" alt="Блины"></td>
            </tr>
            <tr>
                <td>Olivier Salad</td>
                <td>8.5</td>
                <td><a href="https://www.example.com/olivier-salad-recipe" target="_blank">Recipe</a></td>
                <td><img src="https://www.example.com/images/olivier-salad.jpg" alt="Салат Оливье"></td>
            </tr>
            <tr>
                <td>Shchi</td>
                <td>7.5</td>
                <td><a href="https://www.example.com/shchi-recipe" target="_blank">Recipe</a></td>
                <td><img src="https://www.example.com/images/shchi.jpg" alt="Щи"></td>
            </tr>
        </tbody>
    </table>
</body>
</html>
```
