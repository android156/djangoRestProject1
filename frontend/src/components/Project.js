import React from 'react'

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
                {project.link}
            </td>
            <td>
                {project.users}
            </td>
        </tr>
    )
}

const ProjectList = ({projects}) => {
    return (
        <table>
            <th>
                Name
            </th>
            <th>
                Description
            </th>
            <th>
                URL
            </th>
            <th>
                User list
            </th>
            {projects.map((project) => <ProjectItem project={project}/>)}
        </table>
    )
}
export default ProjectList