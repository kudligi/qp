import React from "react";
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import TableCell from '@material-ui/core/TableCell';
import DeleteIcon from '@material-ui/icons/Delete';
import EditIcon from '@material-ui/icons/Edit';
import Done from '@material-ui/icons/Done';
import TextField from "@material-ui/core/TextField";

class Row extends React.Component {
  render() {
    const currentlyEditing = this.props.editIdx === this.props.i;

    return(
      <TableRow>
        {this.props.header.map((y, k) => (
          <TableCell key={k}>
            {currentlyEditing ? (
              <TextField
                name={y.prop}
                onChange={e => this.props.handleChange(e, y.prop, this.props.i)}
                value={this.props.x[y.prop]}
              />
            ) : (
              this.props.x[y.prop]
            )}
          </TableCell>
        ))}
        <TableCell>
          {currentlyEditing ? (
            <Done onClick={() => this.props.stopEditing()} />
          ) : (
            <EditIcon onClick={() => this.props.startEditing(this.props.i)} />
          )}
        </TableCell>
        <TableCell>
          <DeleteIcon onClick={() => this.props.handleRemove(this.props.i)} />
        </TableCell>
      </TableRow>
    );
  }
}

class DataTable extends React.Component {
  render() {
    return (
      <Table>
        <TableHead>
          <TableRow>
            {this.props.header.map((x, i) => (
              <TableCell key={`thc-${i}`}>{x.name}</TableCell>
            ))}
            <TableCell />
            <TableCell />
          </TableRow>
        </TableHead>
        <TableBody>
          {this.props.data.map((x, i) =>
                               <Row
                                 key={i}
                                 x={x}
                                 i={i}
                                 header={this.props.header}
                                 handleChange={this.props.handleChange}
                                 handleRemove={this.props.handleRemove}
                                 startEditing={this.props.startEditing}
                                 stopEditing={this.props.stopEditing}
                                 editIdx={this.props.editIdx}
                               />
                              )
          }
        </TableBody>
      </Table>
    );
  }
}

export default DataTable;
