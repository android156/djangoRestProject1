import React from 'react'
import {generateUniqueID} from "web-vitals/dist/modules/lib/generateUniqueID";


const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>
                {project.name}
            </td>
            <td>
                {project.description}
            </td>
            <td>
                {project.users.map(user => <div key={generateUniqueID()}>{user.user_name}</div>)}
            </td>
            <td>
                {project.link}
            </td>
        </tr>
    )
}

const ProjectList = ({projects}) => {
    return (
        <table>
            <caption>Проекты</caption>
            <thead>
                <tr>
                    <th>
                        Название проекта
                    </th>
                    <th>
                        Описание
                    </th>
                    <th>
                        Участники
                    </th>
                    <th>
                        URL
                    </th>
                </tr>
            </thead>
            <tbody>
                {projects.map((project) => <ProjectItem project={project} key={project.uid}/>)}
            </tbody>
        </table>
    )
}
export default ProjectList