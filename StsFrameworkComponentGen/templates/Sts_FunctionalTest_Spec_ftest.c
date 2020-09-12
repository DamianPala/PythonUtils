/*=======================================================================================*
 * @file    {{module_name}}_ftest.c
 * @brief   This file contains functional tests for {{module_name}} module.
 *======================================================================================*/

/**
 * @addtogroup {{module_name}}_ftest Description
 * @{
 * @brief Functional tests implementation.
 */

/*======================================================================================*/
/*                       ####### PREPROCESSOR DIRECTIVES #######                        */
/*======================================================================================*/
/*-------------------------------- INCLUDE DIRECTIVES ----------------------------------*/

#include "{{module_name}}_ftest.h"

#include "unity.h"
#include "unity_fixture.h"

#include "Sts_Common.h"
#include "Sts_Log.h"
#include "Sts_UnityTtsHelper.h"

#include "{{module_name}}.h"
#include "{{ftest_gen_component_name}}_ftest.h"

/*----------------------------- LOCAL OBJECT-LIKE MACROS -------------------------------*/

/*---------------------------- LOCAL FUNCTION-LIKE MACROS ------------------------------*/

/*======================================================================================*/
/*                      ####### LOCAL TYPE DECLARATIONS #######                         */
/*======================================================================================*/
/*---------------------------- ALL TYPE DECLARATIONS -----------------------------------*/

/*-------------------------------- OTHER TYPEDEFS --------------------------------------*/

/*------------------------------------- ENUMS ------------------------------------------*/

/*------------------------------- STRUCT AND UNIONS ------------------------------------*/

/*======================================================================================*/
/*                    ####### LOCAL FUNCTIONS PROTOTYPES #######                        */
/*======================================================================================*/

static void RunAllTests(void);

static void SetUp(void);

static void TearDown(void);

/*======================================================================================*/
/*                         ####### OBJECT DEFINITIONS #######                           */
/*======================================================================================*/
/*--------------------------------- EXPORTED OBJECTS -----------------------------------*/

/*---------------------------------- LOCAL OBJECTS -------------------------------------*/

/*======================================================================================*/
/*                   ####### LOCAL FUNCTIONS DEFINITIONS #######                        */
/*======================================================================================*/

static void RunAllTests(void)
{
    RUN_TEST_GROUP({{ftest_gen_component_name}}_ftest);
}

/*======================================================================================*/
/*                  ####### SETUP AND TEARDOWN DEFINITIONS #######                      */
/*======================================================================================*/

static void SetUp(void)
{
    /* Add specific setup routines */
}

static void TearDown(void)
{
	/* Add specific teardown routines */
}

/*======================================================================================*/
/*                        ####### TESTS DEFINITIONS #######                             */
/*======================================================================================*/

TEST_GROUP_RUNNER({{ftest_gen_component_name}}_ftest)
{
    RUN_TEST_CASE({{ftest_gen_component_name}}_ftest, ICan_DoSomething);
}

void {{module_name}}_ftest_RunAllTests(void)
{
    {{ftest_gen_component_name}}_ftest_Init(SetUp, TearDown);

    (void)UnityMain(0, NULL, RunAllTests);
}

/**
 * @} end of group {{module_name}}_ftest
 */
