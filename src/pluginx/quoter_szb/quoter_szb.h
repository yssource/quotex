/*
* Copyright (c) 2018-2018 the QuoteX authors
* All rights reserved.
*
* The project sponsor and lead author is Xu Rendong.
* E-mail: xrd@ustc.edu, QQ: 277195007, WeChat: ustc_xrd
* See the contributors file for names of other contributors.
*
* Commercial use of this code in source and binary forms is
* governed by a LGPL v3 license. You may get a copy from the
* root directory. Or else you should get a specific written
* permission from the project author.
*
* Individual and educational use of this code in source and
* binary forms is governed by a 3-clause BSD license. You may
* get a copy from the root directory. Certainly welcome you
* to contribute code of all sorts.
*
* Be sure to retain the above copyright notice and conditions.
*/

#ifndef QUOTER_SZB_QUOTER_SZB_H
#define QUOTER_SZB_QUOTER_SZB_H

#include <string>

#include <plugins/plugins.h>

#include "../../global/compile.h"

class QuoterSZB_P;

class QUOTER_SZB_EXPIMP QuoterSZB : public basicx::Plugins_X
{
public:
	QuoterSZB();
	~QuoterSZB();

public:
	virtual bool Initialize() override;
	virtual bool InitializeExt() override;
	virtual bool StartPlugin() override;
	virtual bool IsPluginRun() override;
	virtual bool StopPlugin() override;
	virtual bool UninitializeExt() override;
	virtual bool Uninitialize() override;
	virtual bool AssignTask( int32_t task_id, int32_t identity, int32_t code, std::string& data ) override;

private:
	QuoterSZB_P* m_quoter_szb_p;

// 自定义成员函数和变量

};

#endif // QUOTER_SZB_QUOTER_SZB_H
