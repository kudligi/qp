import React from 'react';
import { withStyles } from '@material-ui/core/styles';
import MenuItem from '@material-ui/core/MenuItem';
import TextField from '@material-ui/core/TextField';

const styles = theme => ({
  container: {
    display: 'flex',
    flexWrap: 'wrap',
  },
  textField: {
    marginLeft: theme.spacing.unit,
    marginRight: theme.spacing.unit,
    width: 200,
  },
  menu: {
    width: 200,
  },
});

class DiscreteField extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            option: "",
        };
    }

    handleChange = event => {
        this.setState({ option: event.target.value });
    }

    render() {
        const { classes } = this.props;

        return (
            <form className={classes.container} noValidate autoComplete="off">
              <TextField
                select label={this.props.title}
                className={classes.textField}
                value={this.state.option}
                onChange={this.handleChange}
                SelectProps={{
                    MenuProps: {
                        className: classes.menu,
                    },
                }} margin="normal">
                {this.props.options.map((option, index) => (
                    <MenuItem key={index} value={index}>
                      {option}
                    </MenuItem>
                ))}
              </TextField>
            </form>
        );
    }
}

export default withStyles(styles)(DiscreteField);
