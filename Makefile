create-virenv:

	# pip is needed for installing some python packages
	conda create --yes -n cookbook ipython-notebook=2.3.0 \
		pip matplotlib=1.4.2 pandas=0.15.0 xlrd bokeh=0.6.1 \
		selenium=2.42.1 beautiful-soup=4.3.1

clean:

	source deactivate
