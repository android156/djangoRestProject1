import React from 'react'


class TodoForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            user: props.users[0].uid, project: props.projects[0].uid, text: ''
        }
    }

    handleChange(event) {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    }

    handleSubmit(event) {
        this.props.createTodo(this.state.text, this.state.user, this.state.project)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <div
                    className="form-group">
                    <label htmlFor="text">text</label>
                    <input type="text" className="form-control" name="text"
                           value={this.state.text} onChange={(event) => this.handleChange(event)}/>
                </div>
                <div className="form-group">
                    <label htmlFor="user">user</label>
                    <select name="user" className='form-control' onChange={(event) => this.handleChange(event)}>
                        {this.props.users.map((user) => <option value={user.uid}>{user.first_name} {user.last_name}</option>)}
                    </select>
                    {/*<input type="number" className="form-control" name="user"*/}
                    {/*        value={this.state.user} onChange={(event) => this.handleChange(event)}/>*/}
                </div>
                <div className="form-group">
                    <label htmlFor="project">project</label>
                    <select name="project" className='form-control' onChange={(event) => this.handleChange(event)}>
                        {this.props.projects.map((project) => <option value={project.uid}>{project.name}</option>)}
                    </select>
                    {/*<input type="number" className="form-control" name="project"*/}
                    {/*       value={this.state.project} onChange={(event) => this.handleChange(event)}/>*/}
                </div>
                < input type="submit" className="btn btn-primary" value="Save"/>
            </form>
        );
    }
}

export default TodoForm
