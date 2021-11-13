//=====================================
// return survival prob for MARKER score:
//=====================================
float mort(float marker, bool oneYear){

float xsplit; float xmax; float ysplit; float ymax;
float a; float b;
float p0; float p1; float p2; float p3;
float answ;
        
if (oneYear) {
  xsplit = 0.45;
  p0 = 6.78405e-02;
  p1 = 1.36102e+01;
  p2 = 4.58810e-01;
  p3 = 5.94762e-01;
  if (marker < xsplit) {
    answ =  p0*(1-p1*erf((marker-p2)/p3));
  }
  else {
    answ = p0*(1-p1*erf((xsplit-p2)/p3));
    answ = answ * exp(-3*(marker-xsplit));
  }
 }
 else {
   xsplit = -0.2;
   xmax   = 0.33;
   p0 = 8.75449e-01;
   p1 = -4.83189e-01;
   p2 = -1.70824e+00;
   p3 = -6.45576e+00;
   if (marker >= xsplit && marker < xmax) {
     answ = p0 + p1*marker + p2*marker*marker + p3*marker*marker*marker;
   }
   else if (marker < xsplit) {
     ysplit = p0 + p1*xsplit + p2*xsplit*xsplit + p3*xsplit*xsplit*xsplit;
     b      = (ysplit-1)/(xsplit+0.4);
     a      = 1 + 0.4*b;
     answ   = a + b*marker;
     if (marker < -0.4) { answ = 1; }
   }
   else {
     ymax = p0 + p1*xmax + p2*xmax*xmax + p3*xmax*xmax*xmax;
     b    = (ymax-0.22)/(xmax-0.6);
     a    = ymax -xmax*b;
     answ = a + b*marker;
   }
 }
 return answ;
}



