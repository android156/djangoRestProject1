import React from 'react'
import {Link} from "react-router-dom";

const UserItem = ({user}) => {
    return (
        <tr>
            <td>
                {user.first_name}
            </td>
            <td>
                {user.last_name}
            </td>
            <td>
                {user.user_name}
            </td>
            <td>
                {user.email}
            </td>
            <td>
                {user.user_category}
            </td>
            <td>
                <Link to={`${user.uid}/projects`}>Проекты пользователя</Link>
            </td>
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <table>
            <caption>Пользователи</caption>
            <thead>
                <tr>
                    <th>
                        Имя
                    </th>
                    <th>
                        Фамилия
                    </th>
                    <th>
                        Аккаунт
                    </th>
                    <th>
                        Пошта
                    </th>
                    <th>
                        Статус
                    </th>
                </tr>
            </thead>
            <tbody>
                {users.map((user) => <UserItem user={user}  key={user.uid}/>)}
            </tbody>
        </table>
    )
}
export default UserList