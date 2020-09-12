/*=======================================================================================*
 * @file    MyComp_ftest.h
 * @author  Dami Pa
 * @version 0.0.1
 * @date    2020-03-17
 * @brief   Header file for functional test MyComp_ftest module
 *
 *          This file contains API of MyComp_ftest module
 *======================================================================================*/
/*----------------------- DEFINE TO PREVENT RECURSIVE INCLUSION ------------------------*/

#ifndef MY_COMP_FTEST_H_
#define MY_COMP_FTEST_H_

#ifdef __cplusplus
extern "C" {
#endif

/**
 * @addtogroup MyComp_ftest Description
 * @{
 * @brief Module description content...
 */

/*======================================================================================*/
/*                       ####### PREPROCESSOR DIRECTIVES #######                        */
/*======================================================================================*/
/*-------------------------------- INCLUDE DIRECTIVES ----------------------------------*/

/*--------------------------- EXPORTED OBJECT-LIKE MACROS ------------------------------*/

/*-------------------------- EXPORTED FUNCTION-LIKE MACROS -----------------------------*/

/*======================================================================================*/
/*                     ####### EXPORTED TYPE DECLARATIONS #######                       */
/*======================================================================================*/
/*---------------------------- ALL TYPE DECLARATIONS -----------------------------------*/

/*-------------------------------- OTHER TYPEDEFS --------------------------------------*/

/*------------------------------------- ENUMS ------------------------------------------*/

/*------------------------------- STRUCT AND UNIONS ------------------------------------*/

/*======================================================================================*/
/*                    ####### EXPORTED OBJECT DECLARATIONS #######                      */
/*======================================================================================*/

/*======================================================================================*/
/*                   ####### SETUP AND TEARDOWN DECLARATIONS #######                    */
/*======================================================================================*/

/*======================================================================================*/
/*                          ####### TESTS PROTOTYPES #######                            */
/*======================================================================================*/

void MyComp_ftest_Init(void (*set_up_specyfic)(void), void (*tear_down_specyfic)(void));

/**
 * @} end of group MyComp_ftest
 */
 
#ifdef __cplusplus
}
#endif

#endif /* MY_COMP_FTEST_H_ */
