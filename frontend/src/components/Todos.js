import React from 'react'

const TodoItem = ({todo}) => {
    return (
        <tr>
            <td>
                {todo.updated}
            </td>
            <td>
                {todo.text}
            </td>
            <td>
                {todo.user.first_name} {todo.user.last_name}
            </td>
            <td>
                {todo.project.description}
            </td>
            <td>
                {todo.project.description}
            </td>
            <td>
                <button onClick={() => deleteTodo(todo.uid)} type='button'>Delete</button>
            </td>
        </tr>
    )
}

const TodoList = ({todos}) => {
    return (
        <table>
            <caption>Задания</caption>
            <thead>
            <tr>
                <th>
                    Дата изменений
                </th>
                <th>
                    Задание
                </th>
                <th>
                    Исполнитель
                </th>
                <th>
                    Проект
                </th>
                <th>
                </th>
            </tr>
            </thead>
            <tbody>
            {todos.map((todo) => <TodoItem todo={todo} key={todo.uid} deleteTodo={deleteTodo}/>)}
            </tbody>
        </table>
    )
}
export default TodoList