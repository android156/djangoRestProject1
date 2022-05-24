import logo from './logo.svg';
import './App.css';
import React from 'react';
import UserList from './components/User.js'
import axios from 'axios'
import ProjectList from "./components/Project";
import TodoList from "./components/todos";


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todos': [],

        }
    }

    // Заглушка, которая юзеров грузит из списка

    // componentDidMount() {
    //     const users = [
    //         {
    //             'first_name': 'Иван',
    //             'last_name': 'Коротышкин',
    //             'user_name': 'korotkiy',
    //             'email': 'korotkiy@mail.ru',
    //         },
    //         {
    //             'first_name': 'Админ',
    //             'last_name': 'Админов',
    //             'user_name': 'admin',
    //             'email': 'admin@mail.ru',
    //         },
    //     ]
    //     this.setState(
    //         {
    //             'users': users
    //             }
    //     )
    // }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users/')
            .then(response => {
                const users = response.data.results
                this.setState(
                    {
                        'users': users
                    }
                )
            }).catch(error => console.log(error))
        axios.get('http://127.0.0.1:8000/api/projects/')
            .then(response => {
                const projects = response.data.results
                this.setState(
                    {
                        'projects': projects
                    }
                )
            }).catch(error => console.log(error))
        axios.get('http://127.0.0.1:8000/api/todo/')
            .then(response => {
                const todos = response.data.results
                this.setState(
                    {
                        'todos': todos
                    }
                )
            }).catch(error => console.log(error))
    }

    render() {
        return (
            <div>
                <div><UserList users={this.state.users}/></div>
                <div><ProjectList projects={this.state.projects}/></div>
                <div><TodoList todos={this.state.todos}/></div>
            </div>
        )
    }
}

export default App;