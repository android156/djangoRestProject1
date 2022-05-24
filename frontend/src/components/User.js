import React from 'react'

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
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <table>
            <thead>
                <tr>
                    <th>
                        First name
                    </th>
                    <th>
                        Last Name
                    </th>
                    <th>
                        Username
                    </th>
                    <th>
                        E-mail
                    </th>
                    <th>
                        Категория пользователя
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