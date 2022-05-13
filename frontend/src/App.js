import logo from './logo.svg';
import './App.css';
import React from 'react';
import UserList from './components/User.js'


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': []
        }
    }

    componentDidMount() {
        const users = [
            {
                'first_name': 'Иван',
                'last_name': 'Коротышкин',
                'user_name': 'korotkiy',
                'email': 'korotkiy@mail.ru',
            },
            {
                'first_name': 'Админ',
                'last_name': 'Админов',
                'user_name': 'admin',
                'email': 'admin@mail.ru',
            },
        ]
        this.setState(
            {
                'users': users
                }
        )
    }

    render() {
        return (
            <div>
                <UserList users={this.state.users} />
            </div>
        )
    }
}

export default App;