var list_across0 = [
'_contents_xml.htm',
'_reference.xml',
'_index.xml',
'_search_xml.htm',
'_external.xml'
];
var list_up0 = [
'cppad.xml',
'adfun.xml',
'drivers.xml',
'sparse_jacobian.xml'
];
var list_down3 = [
'install.xml',
'introduction.xml',
'ad.xml',
'adfun.xml',
'library.xml',
'preprocessor.xml',
'example.xml',
'appendix.xml'
];
var list_down2 = [
'independent.xml',
'funconstruct.xml',
'dependent.xml',
'seqproperty.xml',
'funeval.xml',
'drivers.xml',
'funcheck.xml',
'omp_max_thread.xml',
'fundeprecated.xml'
];
var list_down1 = [
'jacobian.xml',
'forone.xml',
'revone.xml',
'hessian.xml',
'fortwo.xml',
'revtwo.xml',
'sparse_jacobian.xml',
'sparse_hessian.xml'
];
var list_down0 = [
'sparse_jacobian.cpp.xml'
];
var list_current0 = [
'sparse_jacobian.xml#Syntax',
'sparse_jacobian.xml#Purpose',
'sparse_jacobian.xml#f',
'sparse_jacobian.xml#x',
'sparse_jacobian.xml#p',
'sparse_jacobian.xml#jac',
'sparse_jacobian.xml#BaseVector',
'sparse_jacobian.xml#BoolVector',
'sparse_jacobian.xml#Uses Forward',
'sparse_jacobian.xml#Example'
];
function choose_across0(item)
{	var index          = item.selectedIndex;
	item.selectedIndex = 0;
	if(index > 0)
		document.location = list_across0[index-1];
}
function choose_up0(item)
{	var index          = item.selectedIndex;
	item.selectedIndex = 0;
	if(index > 0)
		document.location = list_up0[index-1];
}
function choose_down3(item)
{	var index          = item.selectedIndex;
	item.selectedIndex = 0;
	if(index > 0)
		document.location = list_down3[index-1];
}
function choose_down2(item)
{	var index          = item.selectedIndex;
	item.selectedIndex = 0;
	if(index > 0)
		document.location = list_down2[index-1];
}
function choose_down1(item)
{	var index          = item.selectedIndex;
	item.selectedIndex = 0;
	if(index > 0)
		document.location = list_down1[index-1];
}
function choose_down0(item)
{	var index          = item.selectedIndex;
	item.selectedIndex = 0;
	if(index > 0)
		document.location = list_down0[index-1];
}
function choose_current0(item)
{	var index          = item.selectedIndex;
	item.selectedIndex = 0;
	if(index > 0)
		document.location = list_current0[index-1];
}