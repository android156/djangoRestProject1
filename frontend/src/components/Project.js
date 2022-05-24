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
        </tr>
    )
}

const ProjectList = ({projects}) => {
    return (
        <table>
            <thead>
                <tr>
                    <th>
                        Name
                    </th>
                    <th>
                        Description
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