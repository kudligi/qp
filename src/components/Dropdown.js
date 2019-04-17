import React from 'react';
import { withStyles } from '@material-ui/core/styles';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import Collapse from '@material-ui/core/Collapse';
import ExpandLess from '@material-ui/icons/ExpandLess';
import ExpandMore from '@material-ui/icons/ExpandMore';

const styles = theme => ({
    root: {
        width: '100%',
        maxWidth: '100%',
        backgroundColor: theme.palette.background.paper,
    },
    nested: {
        paddingLeft: theme.spacing.unit * 3,
    },
});

class DropDown extends React.Component {
    state = {
        open: false,
        selected: "",
    };

    handleClick = () => {
        this.setState(state => ({ open: !state.open }));
    };

    render() {
        const { classes } = this.props;

        return (
            <List component="nav" className={classes.root}>
              <ListItem button onClick={this.handleClick}>
                <ListItemText disableTypography inset primary={this.props.head} />
                {this.state.open ? <ExpandLess /> : <ExpandMore />}
              </ListItem>
              <Collapse in={this.state.open} timeout="auto" unmountOnExit>
                <List component="div" disablePadding>
                  {this.props.list.map((el, index) => (
                      <ListItem button className={classes.nested} key={index} onClick={() => this.props.handleSelect(this.props.head + " " + el)}>
                        <ListItemText inset primary={el}/>
                      </ListItem>
                  ))}
                </List>
              </Collapse>
            </List>
        );
    }
}

export default withStyles(styles)(DropDown);
