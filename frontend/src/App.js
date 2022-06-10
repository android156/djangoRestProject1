import logo from './logo.svg';
import './App.css';
import React from 'react';
import UserList from './components/Users.js'
import axios from 'axios'
import ProjectList from "./components/Projects";
import TodoList from "./components/Todos";
import {BrowserRouter, Route, Routes, Link, Navigate, useLocation} from "react-router-dom";
import UserProjectList from "./components/UserProects";
import LoginForm from "./components/Auth";
import Cookies from 'universal-cookie';
import TodoForm from "./components/TodoForm";

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
            'token': '',

        }
    }

    load_data() {
        const headers = this.get_headers()
        axios.get('http://127.0.0.1:8000/api/users/', {headers})
            .then(response => {
                const users = response.data.results
                this.setState(
                    {
                        'users': users
                    }
                )
            }).catch(error => {
            console.log(error)
            this.setState({'users': []})
        })
        axios.get('http://127.0.0.1:8000/api/projects/', {headers})
            .then(response => {
                const projects = response.data.results
                this.setState(
                    {
                        'projects': projects
                    }
                )
            }).catch(error => {
            console.log(error)
            this.setState({'projects': []})
        })
        axios.get('http://127.0.0.1:8000/api/todo/', {headers})
            .then(response => {
                const todos = response.data.results
                this.setState(
                    {
                        'todos': todos
                    }
                )
            }).catch(error => {
            console.log(error)
            this.setState({'todos': []})
        })
    }

    get_token(username, password) {
        console.log('Получение токена с бэка')
        axios.post('http://127.0.0.1:8000/api-token-auth/', {
            username: username,
            password: password
        })
            .then(response => {
                console.log(response.data)
                console.log('Закидываем токен в куку')
                this.set_token(response.data['token'])

            }).catch(error => alert('Неверный логин или пароль'))
    }

    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, () => this.load_data())
    }

    is_authenticated() {
        return this.state.token !== ''
    }

    logout() {
        this.set_token('')
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, () => this.load_data())
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.is_authenticated()) {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }

    deleteTodo(uid) {
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/todo/${uid}/`, {headers})
            .then(response => {
                this.setState({
                    todos: this.state.todos.filter((todo) => todo.uid !== uid)
                })
            }).catch(error => console.log(error))
    }


    createTodo(text, user, project) {
        const headers = this.get_headers()
        const data = {text: text, user: user, project: project}
        axios.post(`http://127.0.0.1:8000/api/todo/`, data, {headers})
            .then(response => {
                let new_todo = response.data
                const user = this.state.users.filter((user) => user.uid === new_todo.user)[0]
                const project = this.state.projects.filter((project) => project.uid === new_todo.project)[0]
                new_todo.user = user
                new_todo.project = project
                this.setState({todos: [...this.state.todos, new_todo]})
            }).catch(error => console.log(error))
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
        this.get_token_from_storage()
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
                                {this.is_authenticated() ? <button
                                    onClick={() => this.logout()}>Выйти</button> : <Link to='/login'>Войти</Link>}
                            </li>
                        </ul>
                    </nav>
                    <Routes>
                        <Route path='*' element={<NotFound404/>}/>
                        <Route path='/' element={<TodoList todos={this.state.todos}
                                                           deleteTodo={(uid) => this.deleteTodo(uid)}/>}/>
                        <Route path='/create' element={<TodoForm users={this.state.users} projects={this.state.projects}
                                                                 createTodo={(text, user, project) => this.createTodo(text, user, project)}/>}/>
                        <Route path='/users' element={<UserList users={this.state.users}/>}/>
                        <Route path='/users/:uid' element={<UserProjectList projects={this.state.projects}/>}/>}/>
                        <Route path='/projects' element={<ProjectList projects={this.state.projects}/>}/>
                        <Route path='/todo' element={<Navigate to="/" replace/>}/>
                        <Route path='/login' element={<LoginForm
                            get_token={(username, password) => this.get_token(username, password)}/>}/>
                    </Routes>

                </BrowserRouter>
            </div>
        )
    }
}

export default App;