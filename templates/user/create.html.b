<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>User Create</title>
</head>
<body>
    <h1>创建用户</h1>
    <form action="{% url 'user:userCreate' %}" method="post">
        {% csrf_token %}
        <label for="name">用户名：</label>
        <input type="text" name="name" id="name" value="username"></br>

        <label for="password">密码：</label>
        <input type="password" name="password", id="password"></br>

        <label for="sex">性别：</label>
        <input type="radio" name="sex", id="sex" value="0" checked/>男
        <input type="radio" name="sex", id="sex" value="1"/>女</br>

        <input type="submit" value="create">
    </form>
</body>
</html>