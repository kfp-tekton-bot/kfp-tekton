// Code generated by go-swagger; DO NOT EDIT.

package experiment_service

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"context"
	"net/http"
	"time"

	"github.com/go-openapi/errors"
	"github.com/go-openapi/runtime"
	cr "github.com/go-openapi/runtime/client"

	strfmt "github.com/go-openapi/strfmt"
)

// NewDeleteExperimentParams creates a new DeleteExperimentParams object
// with the default values initialized.
func NewDeleteExperimentParams() *DeleteExperimentParams {
	var ()
	return &DeleteExperimentParams{

		timeout: cr.DefaultTimeout,
	}
}

// NewDeleteExperimentParamsWithTimeout creates a new DeleteExperimentParams object
// with the default values initialized, and the ability to set a timeout on a request
func NewDeleteExperimentParamsWithTimeout(timeout time.Duration) *DeleteExperimentParams {
	var ()
	return &DeleteExperimentParams{

		timeout: timeout,
	}
}

// NewDeleteExperimentParamsWithContext creates a new DeleteExperimentParams object
// with the default values initialized, and the ability to set a context for a request
func NewDeleteExperimentParamsWithContext(ctx context.Context) *DeleteExperimentParams {
	var ()
	return &DeleteExperimentParams{

		Context: ctx,
	}
}

// NewDeleteExperimentParamsWithHTTPClient creates a new DeleteExperimentParams object
// with the default values initialized, and the ability to set a custom HTTPClient for a request
func NewDeleteExperimentParamsWithHTTPClient(client *http.Client) *DeleteExperimentParams {
	var ()
	return &DeleteExperimentParams{
		HTTPClient: client,
	}
}

/*DeleteExperimentParams contains all the parameters to send to the API endpoint
for the delete experiment operation typically these are written to a http.Request
*/
type DeleteExperimentParams struct {

	/*ID
	  The ID of the experiment to be deleted.

	*/
	ID string

	timeout    time.Duration
	Context    context.Context
	HTTPClient *http.Client
}

// WithTimeout adds the timeout to the delete experiment params
func (o *DeleteExperimentParams) WithTimeout(timeout time.Duration) *DeleteExperimentParams {
	o.SetTimeout(timeout)
	return o
}

// SetTimeout adds the timeout to the delete experiment params
func (o *DeleteExperimentParams) SetTimeout(timeout time.Duration) {
	o.timeout = timeout
}

// WithContext adds the context to the delete experiment params
func (o *DeleteExperimentParams) WithContext(ctx context.Context) *DeleteExperimentParams {
	o.SetContext(ctx)
	return o
}

// SetContext adds the context to the delete experiment params
func (o *DeleteExperimentParams) SetContext(ctx context.Context) {
	o.Context = ctx
}

// WithHTTPClient adds the HTTPClient to the delete experiment params
func (o *DeleteExperimentParams) WithHTTPClient(client *http.Client) *DeleteExperimentParams {
	o.SetHTTPClient(client)
	return o
}

// SetHTTPClient adds the HTTPClient to the delete experiment params
func (o *DeleteExperimentParams) SetHTTPClient(client *http.Client) {
	o.HTTPClient = client
}

// WithID adds the id to the delete experiment params
func (o *DeleteExperimentParams) WithID(id string) *DeleteExperimentParams {
	o.SetID(id)
	return o
}

// SetID adds the id to the delete experiment params
func (o *DeleteExperimentParams) SetID(id string) {
	o.ID = id
}

// WriteToRequest writes these params to a swagger request
func (o *DeleteExperimentParams) WriteToRequest(r runtime.ClientRequest, reg strfmt.Registry) error {

	if err := r.SetTimeout(o.timeout); err != nil {
		return err
	}
	var res []error

	// path param id
	if err := r.SetPathParam("id", o.ID); err != nil {
		return err
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}
