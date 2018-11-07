import React from 'react';
import {Link, withRouter} from 'react-router-dom';

function Header(props) {
    return (
        <nav className="navbar navbar-dark bg-primary fixed-top">
            <Link className="navbar-brand" to="/">
                JollofJS Documentation App
            </Link>
            <button className="btn btn-dark">Sign In</button>
        </nav>
    )
}

export default withRouter(Header);