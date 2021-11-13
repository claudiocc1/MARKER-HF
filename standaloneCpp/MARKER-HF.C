//-------------------------------------------
// Compile and link on mac with
// clang++ -stdlib=libc++ -o MARKER-HF MARKER-HF.C
//
// Compile and link on linix with
// g++ -std=c++11 -o MARKER-HF MARKER-HF.C
//
// Run it as
// unix> MARKER-HF BPDIAS CREATN BUN HGB WBC PLT ALB RDW
//-----------------------------------------


#include "TMVAClassification_BDT.class.C"
#include <sstream>


int main(int argc, char *argv[]) {

  std::vector<double> in;
  std::vector<std::string> names;

  // Names of variables
  names.push_back("BPDIAS");
  names.push_back("CREATN");
  names.push_back("BUN");
  names.push_back("HGB");
  names.push_back("WBC");
  names.push_back("PLT");
  names.push_back("ALB");
  names.push_back("RDW");

  // Chaeck that number of inputs is correct
  if (argc != 1+names.size() ) {
    std::cout << "Error: needs " << names.size() 
	      << " input parameters, as follows:" << std::endl;
    for (int i=0; i<names.size(); i++ ) std::cout << names[i] << std::endl;
    return -99;
  }

  // Read the parameters and make sure they are numbers
  for (int i=1; i<=names.size(); i++) {
    double thisParameter;
    std::istringstream ss(argv[i]);
 
    if ( !(ss >> thisParameter)) {
	std::cout << "Bad input " << names[i-1] << " = " << argv[i] << std::endl;
	return -99;
      }
      
      in.push_back(thisParameter);

      // check range of input vars:
      if ( names[i-1] == "BPDIAS" && ( in[i-1] < 20 || in[i-1] > 120 ) ) {
          std::cout << "Input out of range: " << names[i-1] << " = " << in[i-1] << std::endl;
          return -99;
      }
      if ( names[i-1] == "CREATN" && ( in[i-1] < 0 || in[i-1] > 25 ) ) {
          std::cout << "Input out of range: " << names[i-1] << " = " << in[i-1] << std::endl;
          return -99;
      }
      if ( names[i-1] == "BUN" && ( in[i-1] < 0 || in[i-1] > 160 ) ) {
          std::cout << "Input out of range: " << names[i-1] << " = " << in[i-1] << std::endl;
          return -99;
      }
      if ( names[i-1] == "HGB" && ( in[i-1] < 2 || in[i-1] > 20 ) ) {
          std::cout << "Input out of range: " << names[i-1] << " = " << in[i-1] << std::endl;
          return -99;
      }
      if ( names[i-1] == "WBC" && ( in[i-1] < 0 || in[i-1] > 40 ) ) {
          std::cout << "Input out of range: " << names[i-1] << " = " << in[i-1] << std::endl;
          return -99;
      }
      if ( names[i-1] == "PLT" && ( in[i-1] < 0 || in[i-1] > 1500 ) ) {
          std::cout << "Input out of range: " << names[i-1] << " = " << in[i-1] << std::endl;
          return -99;
      }
      if ( names[i-1] == "ALB" && ( in[i-1] < 0 || in[i-1] > 6 ) ) {
          std::cout << "Input out of range: " << names[i-1] << " = " << in[i-1] << std::endl;
          return -99;
      }
      if ( names[i-1] == "RDW" && ( in[i-1] < 10 || in[i-1] > 30 ) ) {
          std::cout << "Input out of range: " << names[i-1] << " = " << in[i-1] << std::endl;
          return -99;
      }
      
      // debug
      // std::cout << names[i-1] << " = " << in[i-1] << std::endl;
  }

  ReadBDT thisBDT(names);
  std::cout << thisBDT.GetMvaValue(in) << std::endl;
  return 0;
}
  
