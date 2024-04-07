using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StrategyCalculator.Model.Gpt
{
    /// <summary>
    /// 役割を表現します。
    /// </summary>
    public enum Roles
    {
        /// <summary>
        /// システム。AI に説明を与えます。
        /// </summary>
        System,

        /// <summary>
        /// ユーザー。
        /// </summary>
        User,

        /// <summary>
        /// アシスタント。これは AI です。
        /// </summary>
        Assistant
    }
}
