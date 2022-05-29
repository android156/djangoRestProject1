import logo from './logo.svg';
import './App.css';
import React from 'react';
import UserList from './components/Users.js'
import axios from 'axios'
import ProjectList from "./components/Projects";
import TodoList from "./components/Todos";
import {BrowserRouter, Route, Routes, Link, Navigate, useParams, useLocation} from "react-router-dom";
import UserProjectList from "./components/UserProects";
import LoginForm from "./components/Auth";

const NotFound404 = () => {
    return (
        <div>
            <h1>Страница `{useLocation().pathname}` не найдена</h1>
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

    load_data() {
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

    get_token(username, password) {
        console.log('Запуск get_token')
        axios.post('http://127.0.0.1:8000/api-token-auth/', {
            username: username,
            password: password
        })
            .then(response => {
                console.log(response.data)
            }).catch(error => alert('Неверный логин или пароль'))
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
        this.load_data()
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
                            <li>
                                <Link to='/login'>Войти</Link>
                            </li>
                        </ul>
                    </nav>
                    <Routes>
                        <Route path='*' element={<NotFound404/>}/>
                        <Route path='/' element={<TodoList todos={this.state.todos}/>}/>
                        <Route path='/users' element={<UserList users={this.state.users}/>}/>
                        <Route path='/users/:uid' element={<UserProjectList projects={this.state.projects}/>}/>}/>
                        <Route path='/projects' element={<ProjectList projects={this.state.projects}/>}/>
                        <Route path='/todo' element={<Navigate to="/" replace/>}/>
                        <Route path='/login' element={<LoginForm get_token={(username, password) => this.get_token(username, password)}/>}/>
                    </Routes>

                </BrowserRouter>
            </div>
        )
    }
}

export default App;