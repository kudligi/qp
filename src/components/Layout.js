import React from 'react';
import Sidebar from './Sidebar';

class Layout extends React.Component {
    render() {
        return (
            <div className="layout">
              <Sidebar deps={["dep1", "dep2"]}/>
            </div>
        );
    }
}

export default Layout;
