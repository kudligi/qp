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
        paddingLeft: theme.spacing.unit,
        backgroundColor: theme.palette.background.paper,
    },
    depNested: {
        paddingLeft: theme.spacing.unit * 2,
    },
    paperNested: {
        paddingLeft: theme.spacing.unit * 3,
    },
});

class DropDown extends React.Component {
    state = {
        courseOpen: false,
        depOpen: false,
        selected: "",
    };

    handleCourseClick = () => {
        this.setState(state => ({ courseOpen: !state.courseOpen }));
    };

    handleDepClick = () => {
        this.setState(state => ({ depOpen: !state.depOpen }));
    };

    render() {
        const { classes } = this.props;

        return (
            <List component="div" className={classes.root}>
              <ListItem button onClick={this.handleCourseClick}>
                <ListItemText primary={this.props.course.name} />
                 {this.state.courseOpen ? <ExpandLess /> : <ExpandMore />}
              </ListItem>
              <Collapse in={this.state.courseOpen} timeout="auto" unmountOnExit>
                <List component="div">
                  {this.props.course.deps.map((dep, index) => (
                      <List component="div" key={index}>
                        <ListItem button className={classes.depNested} onClick={this.handleDepClick}>
                          <ListItemText primary={dep.name} className={classes.depNested}/>
                          {this.state.depOpen ? <ExpandLess /> : <ExpandMore />}
                        </ListItem>
                        <Collapse in={this.state.depOpen} timeout="auto" unmountOnExit>
                          <List component="div">
                            {dep.papers.map((paper, index) => (
                                <ListItem button key={index} className={classes.paperNested} onClick={() => this.props.handleSelect(this.props.course.name+dep.name+paper)}>
                                  <ListItemText inset primary={paper}/>
                                </ListItem>
                            ))}
                          </List>
                        </Collapse>
                      </List>
                  ))}
                </List>
              </Collapse>
            </List>
        );
    }
}

export default withStyles(styles)(DropDown);
