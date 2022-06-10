import React from 'react'
import {Link} from "react-router-dom";

const TodoItem = ({todo, deleteTodo}) => {
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
                {todo.project.name}
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

const TodoList = ({todos, deleteTodo}) => {
    return (
        <div>
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
                        Описание проекта
                    </th>
                    <th>
                    </th>
                </tr>
                </thead>
                <tbody>
                {todos.map((todo) => <TodoItem todo={todo} key={todo.uid} deleteTodo={deleteTodo}/>)}
                </tbody>
            </table>
            <Link to='/create'>Create</Link>
        </div>
    )
}
export default TodoList