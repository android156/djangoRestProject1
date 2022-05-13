import logo from './logo.svg';
import './App.css';
import React from 'react';


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': []
        }
    }

    render() {
        return (
            <div>
                Main App
            </div>
        )
    }
}

export default App;