import React from 'react'
import { useParams } from 'react-router-dom'

function contains(arr, elem) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === elem) {
            return true;
        }
    }
    return false;
}

const UserProjectItem = ({project}) => {
    return (
        <tr>
            <td>
                {project.name}
            </td>
            <td>
                {project.description}
            </td>
            <td>
                {project.link}
            </td>
        </tr>
    )
}

const UserProjectList = ({projects}) => {
    let params = useParams();
    let uid = params.uid
    let filtered_projects = projects.filter((project) => contains(project.users.map((user) => user.uid), uid))

    return (
        <table>
            <caption>Проекты пользователя</caption>
            <thead>
                <tr>
                    <th>
                        Название проекта
                    </th>
                    <th>
                        Описание
                    </th>
                    <th>
                        URL
                    </th>
                </tr>
            </thead>
            <tbody>
                {filtered_projects.map((project) => <UserProjectItem project={project} key={project.uid}/>)}
            </tbody>
        </table>
    )
}
export default UserProjectList