import React from 'react'

const TodoItem = ({todo}) => {
    return (
        <tr>
            <td>
                {todo.updated}
            </td>
            <td>
                {todo.user.user_name}
            </td>
            <td>
                {todo.project.description}
            </td>
            <td>
                {todo.text}
            </td>
        </tr>
    )
}

const TodoList = ({todos}) => {
    return (
        <table>
            <thead>
                <tr>
                    <th>
                        Date
                    </th>
                    <th>
                        User
                    </th>
                    <th>
                        Project
                    </th>
                    <th>
                        Text
                    </th>
                </tr>
            </thead>
            <tbody>
                {todos.map((todo) => <TodoItem todo={todo} key={todo.uid}/>)}
            </tbody>
        </table>
    )
}
export default TodoList