import React from 'react';

class Sidebar extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            departments: [],
        };
    }

    render() {
        let deps = this.state.departments ? this.props.deps : [];
        return (
            <ul>
            {deps.map((dep) => {
                return <li>{dep}</li>
            })}
            </ul>
        );
    }
}

export default Sidebar;
