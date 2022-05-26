import logo from './logo.svg';
import './App.css';
import React from 'react';
import UserList from './components/User.js'
import axios from 'axios'
import ProjectList from "./components/Project";
import TodoList from "./components/todos";
import {BrowserRouter, Route, Routes, Link, Redirect, Navigate} from "react-router-dom";

const NotFound404 = ({location}) => {
    return (
        <div>
            {/*<h1>Страница `{location.pathname}` не найдена</h1>*/}
            <h1>Страница не найдена, location в react-router-dom v6 в BrowserRouter не работает </h1>
        </div>
    )
}

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
            <div className="App">
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/'>Задания</Link>
                            </li>
                            <li>
                                <Link to='/users'>Пользователи</Link>
                            </li>
                            <li>
                                <Link to='/projects'>Проекты</Link>
                            </li>
                        </ul>
                    </nav>
                    <Routes>
                        <Route path='*' element={<NotFound404/>}/>
                        <Route path='/' element={<TodoList todos={this.state.todos}/>}/>
                        <Route path='/users' element={<UserList users={this.state.users}/>}/>
                        <Route path='/projects' element={<ProjectList projects={this.state.projects}/>}/>
                        <Route path='/todo' element={<Navigate to="/" replace />}/>
                    </Routes>

                </BrowserRouter>
            </div>
        )
    }
}

export default App;