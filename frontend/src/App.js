import logo from './logo.svg';
import './App.css';
import React from 'react';
import UserList from './components/User.js'
import axios from 'axios'


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': []
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
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            }).catch(error => console.log(error))
    }

    render() {
        return (
            <div>
                <UserList users={this.state.users}/>
            </div>
        )
    }
}

export default App;