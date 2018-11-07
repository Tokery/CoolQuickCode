import React, { Component } from 'react';
import { Route, withRouter } from 'react-router-dom';
import logo from './logo.svg';
import './App.css';
import Header from './Header/Header';
import Welcome from './Welcome/Welcome';
import Page from './Page/Page';

class App extends Component {
  render() {
    return (
      <div>
        <Header />
        <Route exact path='/' component={Welcome} />
        <Route exact path='/page/:page' component={Page} />
      </div>
    );
  }
}

export default App;
